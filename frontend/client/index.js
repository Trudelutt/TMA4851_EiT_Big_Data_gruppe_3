import React, { Component } from 'react';
import { render } from 'react-dom';
import {
  Wrapper,
  GridWrapper,
  footerWrapper,
  ButtonPopulation,
  HeatMap,
  BasicMap,
  TopChart
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

export default class Hello extends Component {
  constructor(props) {
    super(props);
    this.state = {
      basicmapShow: false,
      populationShow: false,
      topChartShow: false,
      value: 3,
    };
    // This binding is necessary to make `this` work in the callback
    this.handleClickPopulation = this.handleClickPopulation.bind(this);
    this.handleClickBasicMap = this.handleClickBasicMap.bind(this);
    this.handleClickTopChart = this.handleClickTopChart.bind(this);
  }

  handleClickPopulation() {
    this.setState({ 
      populationShow: !this.state.populationShow,
      basicmapShow: false,
      topChartShow: false,
    });
    console.log('click');
  }
  handleClickBasicMap() {
    this.setState({ 
      basicmapShow: !this.state.basicmapShow,
      populationShow: false,
      topChartShow: false,
    });
    console.log(this.state);
  }
  handleClickTopChart() {
    this.setState({
      topChartShow: !this.state.topChartShow,
      populationShow: false,
      basicmapShow: false,
    })
  }
  render() {
    return (
      <div>
        <div>
         <MuiThemeProvider>
          <Toolbar style={{marginBottom: 50}}>
        <ToolbarGroup firstChild={true}>
          <RaisedButton label="Lokalitestindex" primary={this.state.populationShow == true ? true : false} onClick={this.handleClickPopulation}/>
          <RaisedButton label="Kart" primary={this.state.basicmapShow == true ? true : false} onClick={this.handleClickBasicMap}/>
          <RaisedButton label="Topp matvarer" primary={this.state.topChartShow == true ? true : false} onClick={this.handleClickTopChart}/>
          <IconMenu
            iconButtonElement={
              <IconButton touch={true}>
                <NavigationExpandMoreIcon />
              </IconButton>
            }
          >
            <MenuItem primaryText="More Info" />
          </IconMenu>
        </ToolbarGroup>
      </Toolbar>
      </MuiThemeProvider>
        </div>

        {this.state.basicmapShow ? (
          <BasicMap />
        ) : this.state.populationShow ? (
          <MuiThemeProvider>
            <HeatMap />
          </MuiThemeProvider>
        ) : this.state.topChartShow ? (
          <TopChart />
      ): (
          <Wrapper />
        )}
       
      </div>
    );
  }
}
render(<Hello />, document.getElementById('app'));
