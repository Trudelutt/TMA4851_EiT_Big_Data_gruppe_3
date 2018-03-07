import styled from 'styled-components';

import app from '../components/App';
import menu from '../components/menu';
//import header from '../components/Header';

export const Wrapper = styled.div`
  height: 100vh;
  color: red;
`;

export const GridWrapper = styled.div`
  display: grid;
  grid-template-columns: 200px;
  grid-template-rows: 100px 100px 20px;
  grid-template-areas: 'righttop' 'center' 'centerBottom bottom';
`;

export const Header = styled.div`
  height: 50px;
  text-align: rightBottom;
  font-size: 28px;
  color: black;
  grid-area: righttop;
  background-color: #5a6572;
  border-bottom: 5px solid #910505;
`;
export const ButtonPopulation = styled.button`
  height: 50px;
  text-align: center;
  font-size: 28px;
  color: black;
  grid-area: centerBottom;
  background-color: #5a6572;
`;
export const ButtonTest = styled.button`
  height: 50px;
  text-align: center;
  font-size: 28px;
  color: black;
  grid-area: bottom;
  background-color: #5a6572;
`;
export const MenuBar = styled(menu)`
  grid-area: top;
  width: 1000px;
  height: auto;
`;

export const App = styled(app)`
  grid-area: center;
  background-color: #383f47;
`;
