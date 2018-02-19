import React, { Component } from 'react';
import { render } from 'react-dom';
import { Wrapper, GridWrapper, App, Visualization } from './elements';

export default class Hello extends Component {
  render() {
    return (
      <Wrapper>
        <App />,
        <Visualization data={['test']} />
      </Wrapper>
    );
  }
}

render(<Hello />, document.getElementById('app'));
