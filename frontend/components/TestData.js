import React, { Component } from 'react';

export default class TestData extends Component {
  constructor(props) {
    super(props);
    this.state = { locations: [] };
  }

    componentDidMount() {
      fetch('http://localhost:5000/testdata', {
        method: "GET",
        headers: {
          "Accept": "application/json",
          "Content-Type": "application/json",
        }
      })
        .then(results => results.json())
        .then(data => {
          console.log('test');
          const locations = data.map(entry => entry.name);
          this.setState( {locations} );
        })
      }

    render() {
      return (
        <div>
          {this.state.locations.map(name => (<li>{name}</li>))}
        </div>
      );
    }
}
