import React, { Component } from 'react';
import { render } from 'react-dom';
import { Wrapper, GridWrapper, App, Visualization } from './elements';
import { slide as Menu } from 'react-burger-menu'

export default class Hello extends Component {
  constructor (props) {
   super(props)
   this.state = {
     menuOpen: false
   }
 }

 // This keeps your state in sync with the opening/closing of the menu
 // via the default means, e.g. clicking the X, pressing the ESC key etc.
 handleStateChange (state) {
   this.setState({menuOpen: state.isOpen})
 }

 // This can be used to close the menu, e.g. when a user clicks a menu item
 closeMenu () {
   this.setState({menuOpen: false})
 }

 // This can be used to toggle the menu, e.g. when using a custom icon
 // Tip: You probably want to hide either/both default icons if using a custom icon
 // See https://github.com/negomi/react-burger-menu#custom-icons
 toggleMenu () {
   this.setState({menuOpen: !this.state.menuOpen})
 }
  render() {
    return (
      <Wrapper>
      <Menu>
          <Menu width={ '20%' } />
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
