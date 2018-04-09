import React, { Component } from 'react';
import Slider from 'material-ui/Slider';

/**
* You may find yourself needing a custom scale.
* Here is how you would implement a [logarithmic scale](https://simple.wikipedia.org/wiki/Logarithmic_scale).
*/
export default class SliderExampleCustomScale extends Component {
  constructor(props) {
    super(props);
    this.state = {
      slider: 1986
    };
    this.handleSlider = this.handleSlider.bind(this);
  }
  handleSlider(event, value) {
    this.setState({ slider: value });
  }

  render() {
    return (
      <div>
        <Slider
          min={1986}
          max={2013}
          step={1}
          value={this.state.slider}
          onChange={this.handleSlider}
        />
        <p>
          <span>{'The value of this slider is: '}</span>
          <span>{this.state.slider}</span>
        </p>
      </div>
    );
  }
}
