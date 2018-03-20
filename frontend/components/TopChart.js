import React, {Component} from 'react';
import {Line} from 'react-chartjs-2';
import data from '../static/topp.json';

console.log(data)

const reduced = Object.values(data).reduce((acc, current) => {
	current.forEach(({ foodItem, tonnes }) => {
      if (!acc[foodItem]) {
		acc[foodItem] = [];
	  }
	  acc[foodItem].push(tonnes);
    });
	return acc;
}, {});

const mapped = Object.entries(reduced).map(([key, value]) => ({ label: key, data: value }));
console.log(mapped);

class TopChart extends Component {
    
    render() {
        return (
            <div>
                <h2>Line Example</h2>
                <Line
                    data={{
                    labels: Object.keys(data),
                    datasets: mapped,
                }}/>
            </div>
        );
    }
};

export default TopChart;