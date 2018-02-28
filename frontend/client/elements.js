import styled from 'styled-components';

import app from '../components/App';
import menu from '../components/menu';

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
  width: 100px;
  height: auto;
`;
export const App = styled(app)`
  position: absolute;
  width: 75vw;
  height: 75vh;
  z-index: -10;
  background-color: red;
`;
