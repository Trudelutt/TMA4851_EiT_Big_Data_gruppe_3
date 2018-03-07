import React, { Component } from 'react';
import { render } from 'react-dom';
import {
  Wrapper,
  GridWrapper,
  ButtonPopulation,
  App,
  MenuBar,
  Header,
  ButtonTest
} from './elements';
import { slide as Menu } from 'react-burger-menu';

var menu_styles = {
  bmMenu: {
    background: '#FF1493',
    padding: '2.5em 1.5em 0',
    fontSize: '1.15em'
  },
  bmBurgerButton: {
    position: 'fixed',
    width: '70px',
    height: '30px',
    left: '36px',
    top: '36px',
    background: '#FF1493'
  }
};

export default class Hello extends Component {
  constructor(props) {
    super(props);
    this.state = {
      populationShow: false
    };
    // This binding is necessary to make `this` work in the callback
    this.handleClickPopulation = this.handleClickPopulation.bind(this);
  }

  handleClickPopulation() {
    this.setState({ populationShow: !this.state.populationShow });
    console.log('click');
  }

  render() {
    return (
      <GridWrapper>
        {this.state.populationShow ? <App /> : null}

        <ButtonPopulation onClick={this.handleClickPopulation}>
          {'Population'}
        </ButtonPopulation>
      </GridWrapper>
    );
  }
}
render(<Hello />, document.getElementById('app'));
