import styled from 'styled-components';

import app from '../components/App';
import menu from '../components/menu';
//import header from '../components/Header';

export const Wrapper = styled.div`
  height: 100vh;
  color: red;
`;

export const GridWrapper = styled.div`
  pointer-events: none;
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  overflow: hidden;
  display: grid;
  grid-template-columns: 1fr 200px;
  grid-template-rows: 1fr 120px 100px 20px;
  grid-template-areas: 'top right' 'center rightBottom'
    'centerBottom rightBottom' 'margin margin';
`;
export const MenuBar = styled(menu)`
  grid-area: top;
  width: 1000px;
  height: auto;
`;
export const Header = styled.div`
  height: 50px;
  text-align: center;
  font-size: 28px;
  color: black;
  grid-area: right;
  background-color: white;
  border-bottom: 5px solid blue;
`;
export const App = styled(app)`grid-area: center;`;
