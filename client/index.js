import React, { Component } from 'react';
import { render } from 'react-dom';
import { Wrapper } from './elements';
import Visualization from '../component/visualization';

export default class Hello extends Component {
  render() {
    return (
      <Wrapper>
        <Visualization data={['test']} />
      </Wrapper>
    );
  }
}

render(<Hello />, document.getElementById('app'));
