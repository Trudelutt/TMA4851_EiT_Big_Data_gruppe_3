import React, { Component } from 'react';
import {
  ComposableMap,
  ZoomableGroup,
  Geographies,
  Geography
} from 'react-simple-maps';
import { scaleLinear } from 'd3-scale';
import map from '../static/heatmap.json';
import locality from '../static/locality.json';
import Slider from 'material-ui/Slider';
import IndexChartDialog from './IndexChartDialog';
import minmax from '../static/min_max_locality.json';

const wrapperStyles = {
  width: '80%',
  margin: '0 auto'
};

const popScale = scaleLinear()
  .domain([
    0,
    0.001,
    0.0015,
    0.002,
    0.0025,
    0.003,
    0.0035,
    0.004,
    0.0045,
    0.005,
    0.006,
    0.007,
    0.008,
    0.009,
    0.01,
    0.02,
    0.03,
    0.04,
    0.05,
    0.06,
    0.07,
    0.08,
    0.09,
    0.1
  ])
  .range([
    '#FFFFFF',
    '#7BD1F9',
    '#6FC7F0',
    '#69C3EC',
    '#5FBBE5',
    '#57B5E0',
    '#55B6E4',
    '#52B2DE',
    '#49ACDA',
    '#46A9D7',
    '#3CA7D9',
    '#35A4D8',
    '#2B9FD5',
    '#2FA4D9',
    '#1999D4',
    '#1B95CF',
    '#1483B6'
  ]);

const MIN_YEAR = 1986;
const MAX_YEAR = 2013;

const WhiteTextParagraph = ({ children }) => (
    <p style={{ color: 'white' }}>{children}</p>
);

class HeatMap extends Component {
  constructor(props) {
    super(props);

    this.state = {
      slider: MIN_YEAR,
      currentCountry: undefined,
      open: false
    };

    this.handleSlider = this.handleSlider.bind(this);
    this.handleOpen = this.handleOpen.bind(this);
    this.handleClose = this.handleClose.bind(this);
  }

  componentDidMount() {
      const range = [...Array(MAX_YEAR - MIN_YEAR).keys()];
      range.forEach((item, index) => {
         setTimeout(() => {
             this.setState(state => ({
                 slider: state.slider + 1
             }));
         }, 1500 * (index + 1));
      });
  }


  handleSlider(e, value) {
    this.setState({ slider: parseInt(value) });
  }

  handleOpen(country) {
    const values = Object.entries(country.properties)
      .filter(([key, value]) => key.startsWith('year_'))
      .reduce((accumulated, [key, value]) => {
        accumulated[key.substring(5)] = value;
        return accumulated;
      }, {});

    this.setState({
      currentCountry: {
        name: country.properties.name_long,
        values
      },
      open: true
    });
  }

  handleClose() {
    this.setState({
      currentCountry: undefined,
      open: false
    });
  }

  render() {
    const { slider, currentCountry, open } = this.state;
    return (
      <div style={wrapperStyles}>
        <WhiteTextParagraph>
            <span style={{ fontSize: '50px' }}>{slider}</span>
        </WhiteTextParagraph>
        <ComposableMap
          projectionConfig={{
            scale: 120,
            rotation: [-11, 0, 0]
          }}
          width={980}
          height={300}
          style={{
            width: '100%',
            height: 'auto'
          }}
        >
          <ZoomableGroup center={[0, 20]}>
            <Geographies geography={map} disableOptimization>
              {(geographies, projection) =>
                geographies.map((geography, i) => (
                  <Geography
                    key={i}
                    geography={geography}
                    projection={projection}
                    onClick={this.handleOpen}
                    style={{
                      default: {
                        fill: popScale(geography.properties['year_' + slider]),
                        stroke: '#607D8B',
                        strokeWidth: 0.75,
                        outline: 'none'
                      }
                    }}
                  />
                ))}
            </Geographies>
          </ZoomableGroup>
        </ComposableMap>
        <Slider
          min={MIN_YEAR}
          max={MAX_YEAR}
          step={1}
          value={slider}
          onChange={this.handleSlider}
        />
        <WhiteTextParagraph>
          <br />
          <span>Min:&nbsp;{`${minmax[`year_${slider}`]['min_name']} ${minmax[`year_${slider}`]['min_value']}`}</span>
          <br />
          <span>Max:&nbsp;{`${minmax[`year_${slider}`]['max_name']} ${minmax[`year_${slider}`]['max_value']}`}</span>
        </WhiteTextParagraph>

        {currentCountry && (
          <IndexChartDialog
            country={currentCountry}
            open={open}
            handleClose={this.handleClose}
          />
        )}
      </div>
    );
  }
}

export default HeatMap;
