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
const wrapperStyles = {
  width: '100%',
  maxWidth: 1200,
  margin: '0 auto'
};

const popScale = scaleLinear()
  .domain([0, 0.001, 0.01, 0.5, 1])
  .range(['#F6EE90', '#FFC640', '#F37E3B', '#910505', '#C30101']);

class HeatMap extends Component {
  constructor(props) {
    super(props);
    this.state = {
      slider: 1995
    };
    this.handleSlider = this.handleSlider.bind(this);
  }
  handleSlider(event, value) {
    console.log('year_' + 1995);
    console.log('year_' + this.state.slider);
    this.setState({ slider: parseInt(value) });
  }
  render() {
    return (
      <div style={wrapperStyles}>
        <div>
          <ComposableMap
            projectionConfig={{
              scale: 205,
              rotation: [-11, 0, 0]
            }}
            width={980}
            height={500}
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
                      onClick={this.handleClick}
                      style={{
                        default: {
                          fill: popScale(
                            geography.properties['year_' + this.state.slider]
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
            value={this.state.slider}
            onChange={this.handleSlider}
          />
          <p>
            <span>{'Year: '}</span>
            <span>{this.state.slider}</span>
          </p>
        </div>
      </div>
    );
  }
}

export default HeatMap;
