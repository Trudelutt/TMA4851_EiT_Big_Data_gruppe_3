import React, { Component } from 'react';
import { render } from 'react-dom';
import BasicMap from '../components/BasicMap';
import { Tooltip, actions } from 'redux-tooltip';

class App extends Component {
  render() {
    return (
      <div>
        <BasicMap>
          <Tooltip>Hello Tooltip!</Tooltip>
        </BasicMap>
      </div>
    );
  }
}

export default App;
