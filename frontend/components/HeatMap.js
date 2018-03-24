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

const wrapperStyles = {
    width: '100%',
    maxWidth: 1200,
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

class HeatMap extends Component {
    constructor(props) {
        super(props);

        this.state = {
            slider: 1986,
            currentCountry: undefined,
            open: false
        };

        this.handleSlider = this.handleSlider.bind(this);
        this.handleOpen = this.handleOpen.bind(this);
        this.handleClose = this.handleClose.bind(this);
    }

    handleSlider(e, value) {
        console.log('year_' + 1995);
        console.log('year_' + this.state.slider);
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
                          fill: popScale(
                            geography.properties['year_' + slider]
                          ),
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
                    min={1986}
                    max={2013}
                    step={1}
                    value={slider}
                    onChange={this.handleSlider}
                />
                <p>
                    <span>{'Year: '}</span>
                    <span>{slider}</span>
                </p>
                {currentCountry &&
                <IndexChartDialog
                    country={currentCountry}
                    open={open}
                    handleClose={this.handleClose}
                />}
            </div>
        );
    }
}

export default HeatMap;
