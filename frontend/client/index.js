import React, { Component } from 'react';
import { render } from 'react-dom';
import {
  Wrapper,
  GridWrapper,
  footerWrapper,
  ButtonPopulation,
  HeatMap,
  BasicMap
} from './elements';
import { slide as Menu } from 'react-burger-menu';

export default class Hello extends Component {
  constructor(props) {
    super(props);
    this.state = {
      basicmapShow: false,
      populationShow: false
    };
    // This binding is necessary to make `this` work in the callback
    this.handleClickPopulation = this.handleClickPopulation.bind(this);
    this.handleClickBasicMap = this.handleClickBasicMap.bind(this);
  }

  handleClickPopulation() {
    this.setState({ populationShow: !this.state.populationShow });
    this.setState({ basicmapShow: false });
    console.log('click');
  }
  handleClickBasicMap() {
    this.setState({ basicmapShow: !this.state.basicmapShow });
    this.setState({ populationShow: false });
    console.log(this.state);
  }

  render() {
    return (
      <GridWrapper>
        {this.state.basicmapShow ? (
          <BasicMap />
        ) : this.state.populationShow ? (
          <HeatMap />
        ) : (
          <Wrapper />
        )}
        <footerWrapper>
          <ButtonPopulation onClick={this.handleClickPopulation}>
            {'Population'}
          </ButtonPopulation>
          <ButtonPopulation onClick={this.handleClickBasicMap}>
            {'BasicMap'}
          </ButtonPopulation>
        </footerWrapper>
      </GridWrapper>
    );
  }
}
render(<Hello />, document.getElementById('app'));
