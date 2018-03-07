import React, { Component } from 'react';
import {
  ComposableMap,
  ZoomableGroup,
  Geographies,
  Annotation,
  Geography
} from 'react-simple-maps';
import { scaleLinear } from 'd3-scale';
import map from '../static/world-50m.json';

const wrapperStyles = {
  width: '100%',
  maxWidth: 980,
  margin: '0 auto'
};

class BasicMap extends Component {
  render() {
    return (
      <div style={wrapperStyles}>
        <ComposableMap>
          <ZoomableGroup center={[0, 20]}>
            <Geographies geography={map}>
              {(geographies, projection) =>
                geographies.map((geography, i) => (
                  <Geography
                    key={i}
                    geography={geography}
                    projection={projection}
                    onClick={this.handleClick}
                    style={{
                      default: {
                        fill: '#F6EE90',
                        stroke: '#607D8B',
                        strokeWidth: 0.75,
                        outline: 'none'
                      },
                      hover: {
                        fill: '#263238',
                        stroke: '#607D8B',
                        strokeWidth: 0.75,
                        outline: 'none'
                      },
                      pressed: {
                        fill: '#263238',
                        stroke: '#607D8B',
                        strokeWidth: 0.75,
                        outline: 'none'
                      }
                    }}
                  />
                ))}
            </Geographies>
            <Annotation dx={-10} dy={-10} subject={[8.5, 47.3]} strokeWidth={1}>
              <text>{'Zurich'}</text>
            </Annotation>
          </ZoomableGroup>
        </ComposableMap>
      </div>
    );
  }
}

export default BasicMap;
