import React, { Component } from 'react';
import {
  ComposableMap,
  ZoomableGroup,
  Geographies,
  Geography
} from 'react-simple-maps';
import ReactTooltip from 'react-tooltip';
import map from '../static/world-50m.json';

const wrapperStyles = {
  width: '100%',
  margin: '0 auto'
};

class BasicMap extends Component {
  getDOMNode() {
    setTimeout(() => {
      ReactTooltip.rebuild();
    }, 100);
  }
  render() {
    return (
      <div style={wrapperStyles}>
        <ComposableMap
          projectionConfig={{
            scale: 105
          }}
          width={980}
          height={551}
          style={{
            width: '100%',
            height: 'auto'
          }}
        >
          <ZoomableGroup center={[0, 20]} disablePanning>
            <Geographies geography={map}>
              {(geographies, projection) =>
                geographies.map(
                  (geography, i) =>
                    geography.id !== 'ATA' && (
                      <Geography
                        key={i}
                        data-tip={geography.properties.name}
                        geography={geography}
                        projection={projection}
                        style={{
                          default: {
                            fill: '#EAEDEF',
                            stroke: '#4B616B',
                            strokeWidth: 0.8,
                            outline: 'none'
                          },
                          hover: {
                            fill: '#4B616B',
                            stroke: '#4B616B',
                            strokeWidth: 0.75,
                            outline: 'none'
                          },
                          pressed: {
                            fill: '#294C5D',
                            stroke: '#294C5D',
                            strokeWidth: 0.75,
                            outline: 'none'
                          }
                        }}
                      />
                    )
                )}
            </Geographies>
          </ZoomableGroup>
        </ComposableMap>
        <ReactTooltip />
      </div>
    );
  }
}

export default BasicMap;
