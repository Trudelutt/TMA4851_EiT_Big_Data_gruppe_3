import React, { Component } from 'react';
import { render } from 'react-dom';
import { Wrapper, GridWrapper, App, Visualization } from './elements';
import { slide as Menu } from 'react-burger-menu'

export default class Hello extends Component {
  render() {
    return (
      <Wrapper>
        <Menu>
          <a id="home" className="menu-item" href="/">Home</a>
          <a id="about" className="menu-item" href="/about">About</a>
          <a id="contact" className="menu-item" href="/contact">Contact</a>
          <a onClick={ this.showSettings } className="menu-item--small" href="">Settings</a>
        </Menu>
        <GridWrapper>
          <Visualization data={['Hva skjer?']} />
        </GridWrapper>
        <App />
      </Wrapper>
    );
  }
}


render(<Hello />, document.getElementById('app'));
//render(<Example />, document.getElementById('app'));
