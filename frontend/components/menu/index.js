import { slide as Menu } from 'react-burger-menu';
import React, { Component } from 'react';
import { render } from 'react-dom';
import { Wrapper } from './elements';
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

export default class MenuBar extends Component {
  constructor(props) {
    super(props);
    this.state = {
      menuOpen: false
    };
  }
  showSettings(e) {
    // ori
    e.preventDefault();
    console.log(e.type);
    console.log('hei ');
  }

  // This keeps your state in sync with the opening/closing of the menu
  // via the default means, e.g. clicking the X, pressing the ESC key etc.
  handleStateChange(state) {
    this.setState({ menuOpen: state.isOpen });
  }

  // This can be used to close the menu, e.g. when a user clicks a menu item
  closeMenu() {
    this.setState({ menuOpen: false });
  }

  // This can be used to toggle the menu, e.g. when using a custom icon
  // Tip: You probably want to hide either/both default icons if using a custom icon
  // See https://github.com/negomi/react-burger-menu#custom-icons
  toggleMenu() {
    this.setState({ menuOpen: !this.state.menuOpen });
    console.log('hei');
  }

  render() {
    return (
      <Wrapper>
        <Menu
          width={'20%'}
          noOverlay
          //customBurgerIcon={ <img src="index.jpeg" /> }
          customCrossIcon={<img src="index.jpeg" />}
          styles={menu_styles}
          burgerButtonClassName={'fa fa-user fa-2x'}
          customBurgerIcon={<span className="fa fa-user fa-2x" />}
        >
          <a id="home" className="menu-item" href="/">
            Home
          </a>
        </Menu>
      </Wrapper>
    );
  }
}
