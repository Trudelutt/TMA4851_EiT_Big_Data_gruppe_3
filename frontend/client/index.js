import React, { Component } from 'react';
import { render } from 'react-dom';
import {
    Wrapper,
    GridWrapper,
    footerWrapper,
    ButtonPopulation,
    HeatMap,
    BasicMap,
    TopChart,
} from './elements';
import Annotations from 'react-simple-maps';
import markers from '../components/BasicMap';
import { slide as Menu } from 'react-burger-menu';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import IconMenu from 'material-ui/IconMenu';
import IconButton from 'material-ui/IconButton';
import FontIcon from 'material-ui/FontIcon';
import NavigationExpandMoreIcon from 'material-ui/svg-icons/navigation/expand-more';
import MenuItem from 'material-ui/MenuItem';
import DropDownMenu from 'material-ui/DropDownMenu';
import RaisedButton from 'material-ui/RaisedButton';
import {Toolbar, ToolbarGroup, ToolbarSeparator, ToolbarTitle} from 'material-ui/Toolbar';

const MyButton = ({ label, value, onClick, show }) => (
    <RaisedButton primary={show === value} value={value} { ...{ label, onClick } } />
);

export default class Hello extends Component {
  constructor(props) {
    super(props);
    this.state = {
      show: undefined,
      value: 3
    };

    // This binding is necessary to make `this` work in the callback
    this.handleClick = this.handleClick.bind(this);
    this.getChart = this.getChart.bind(this);
  }

  handleClick(e) {
    this.setState({
      show: e.currentTarget.value
    })
  }

  getChart() {
    switch (this.state.show) {
      case "population":
        return (
            <MuiThemeProvider>
              <HeatMap />
            </MuiThemeProvider>
        );
      case "basicMap":
        return <BasicMap />;
      case "topChart":
        return <TopChart />;
      default:
        return <Wrapper />;
    }
  }

  render() {
    const { show } = this.state;
    const buttons = [
      { label: "Lokalitetsindex", value: "population" },
      { label: "Kart", value: "basicMap" },
      { label: "Topp matvarer", value: "topChart" }
    ];
    return (
        <div>
          <MuiThemeProvider>
            <Toolbar style={{marginBottom: 50}}>
              <ToolbarGroup firstChild={true}>
                {buttons.map(({ label, value }) => <MyButton key={value} onClick={this.handleClick} { ...{ show, value, label } } />)}
                <IconMenu
                    iconButtonElement={
              <IconButton touch>
                <NavigationExpandMoreIcon />
              </IconButton>
            }
                >
                  <MenuItem primaryText="More Info" />
                </IconMenu>
              </ToolbarGroup>
            </Toolbar>
          </MuiThemeProvider>
          {this.getChart()}
        </div>
    );
  }
}
render(<Hello />, document.getElementById('app'));
