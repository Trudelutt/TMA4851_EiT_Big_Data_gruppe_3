import React, { Component } from 'react';
import { render } from 'react-dom';
import { Wrapper, GridWrapper, App, MenuBar } from './elements';
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
  render() {
    return (
      <Wrapper>
        <MenuBar />
        <GridWrapper />

        <App />
      </Wrapper>
    );
  }
}
render(<Hello />, document.getElementById('app'));
//render(<Example />, document.getElementById('app'));
