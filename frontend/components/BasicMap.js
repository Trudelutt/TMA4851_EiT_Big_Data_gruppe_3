import React, { Component } from 'react';
import {
  ComposableMap,
  ZoomableGroup,
  Geographies,
  Annotation,
  Annotations,
  Markers,
  Marker,
  Geography
} from 'react-simple-maps';
import { scaleLinear } from 'd3-scale';
import map from '../static/world-50m.json';
import contry from '../static/convertcsv.json';

const wrapperStyles = {
  width: '100%',
  maxWidth: 980,
  margin: '0 auto'
};
const markers = [
  {
    markerOffset: -25,
    name: 'Buenos Aires',
    coordinates: [-58.3816, -34.6037]
  },
  {
    markerOffset: -25,
    name: 'La Paz',
    coordinates: [-68.1193, -16.4897],
    dx: 200,
    dy: -100
  },
  {
    markerOffset: 35,
    name: 'Brasilia',
    coordinates: [-47.8825, -15.7942],
    dx: 200,
    dy: -100
  },
  {
    markerOffset: 35,
    name: 'Santiago',
    coordinates: [-70.6693, -33.4489],
    dx: 200,
    dy: -100
  },
  {
    markerOffset: 35,
    name: 'Bogota',
    coordinates: [-74.0721, 4.711],
    dx: 200,
    dy: -100
  },
  {
    markerOffset: 35,
    name: 'Quito',
    coordinates: [-78.4678, -0.1807],
    dx: 200,
    dy: -100
  },
  {
    markerOffset: -25,
    name: 'Georgetown',
    coordinates: [-58.1551, 6.8013],
    dx: 200,
    dy: -100
  },
  {
    markerOffset: -25,
    name: 'Asuncion',
    coordinates: [-57.5759, -25.2637],
    dx: 200,
    dy: -100
  },
  {
    markerOffset: 35,
    name: 'Paramaribo',
    coordinates: [-55.2038, 5.852],
    dx: 200,
    dy: -100
  },
  {
    markerOffset: 35,
    name: 'Montevideo',
    coordinates: [-56.1645, -34.9011],
    dx: 200,
    dy: -100
  },
  {
    markerOffset: -25,
    name: 'Caracas',
    coordinates: [-66.9036, 10.4806],
    dx: 200,
    dy: -100
  }
];

class BasicMap extends Component {
  constructor(props) {
    super(props);
    this.state = {
      Animation: false
    };
    this.handleClickAnimation = this.handleClickAnimation.bind(this);
  }
  handleClickAnimation() {
    this.setState({ Animation: !this.state.Animation });
  }
  render() {
    return (
      <div style={wrapperStyles}>
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

            {this.state.Animation ? (
              <Annotations>
                {contry.map((contry, i) => (
                  <Annotation
                    key={i}
                    dx={1}
                    dy={1}
                    subject={[contry.CapitalLongitude, contry.CapitalLatitude]}
                    strokeWidth={5}
                    stroke={'#FF5722'}
                    curve={2}
                  />
                ))}
              </Annotations>
            ) : (
              <div />
            )}
          </ZoomableGroup>
        </ComposableMap>
        <button onClick={this.handleClickAnimation}> {'Animation'} </button>
      </div>
    );
  }
}

export default BasicMap;
