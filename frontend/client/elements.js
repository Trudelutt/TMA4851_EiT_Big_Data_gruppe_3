import styled from 'styled-components';
import basicmap from '../components/BasicMap';
import heatmap from '../components/HeatMap';
import topchart from '../components/TopChart';
import indexchartdialog from '../components/IndexChartDialog';
import menu from '../components/menu';
//import header from '../components/Header';

export const GridWrapper = styled.div`
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 550px 70px;
  grid-template-areas: 'center' 'footer';
  height: 100vh;
  width: 100vw;
`;

export const Wrapper = styled.div`grid-area: center;`;

export const footerWrapper = styled.div`
  grid-area: footer;
  height: 70px;
  width: auto;
  background-color: blue;
`;

export const HeatMap = styled(heatmap)`grid-area: center;`;
export const TopChart = styled(topchart)`grid-area: center;`;
export const BasicMap = styled(basicmap)`grid-area: center;`;
export const IndexChartDialog = styled(indexchartdialog)`grid-area: center;`;

export const ButtonPopulation = styled.button`
  text-align: center;
  width: 150px;
  height: 70px;
  font-size: 28px;
  color: black;
  background-color: #5a6572;
`;
