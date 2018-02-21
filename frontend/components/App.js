import React, { Component } from 'react';
import { render } from 'react-dom';
import BasicMap from '../components/BasicMap'
import TestData from '../components/TestData'

class App extends Component {
  render() {
    return (
      <div>
      <TestData></TestData>
      <BasicMap></BasicMap>
      </div>
    );
  }
}

export default App
