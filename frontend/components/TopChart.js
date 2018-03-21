import React, {Component} from 'react';
import {Line} from 'react-chartjs-2';
import data from '../static/topp.json';

console.log(data)

const colors = ["#fff5f5","#ffe3e3","#ffc9c9","#ffa8a8","#ff8787","#edf2ff","#dbe4ff","#bac8ff","#88ABC2","#49708A","#748ffc","#e7f5ff","#d0ebff","#a5d8ff","#4dabf7","#1c7ed6","#e3fafc","#c5f6fa","#99e9f2","#3bc9db", "#22b8cf","#0c8599","#ACCE91","#e6fcf5","#c3fae8","##96f2d7","#20c997","#099268","#d3f9d8","#8ce99a", "#69db7c","#40c057","#2f9e44","#d8f5a2","#a9e34b", "#82c91e","#fff9db","#fff3bf","#ffec99","#ffe066", "#ffd43b","#fcc419","#fab005","#f08c00","#087f5b", "#0b7285","#1864ab","#d0bfff","#cc5de8","#a61e4d",'#da77f2','#c2255c' ]

const reduced = Object.values(data).reduce((acc, current) => {
	current.forEach(({ foodItem, tonnes }) => {
      if (!acc[foodItem]) {
		acc[foodItem] = [];
	  }
	  acc[foodItem].push(tonnes);
    });
	return acc;
}, {});

const mapped = Object.entries(reduced).map(([key, value], index) => ({ label: key, data: value, borderColor: colors[index]}));

/* backgroundColor: colors[indexOf()] total matforbruk og total kjøttforbruk, like hvis de har like stor andel som er kjtøt*/

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