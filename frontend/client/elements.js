import styled from 'styled-components';

import Viz from '../components/visualization';
import app from '../components/App';

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
export const Visualization = styled(Viz)`
  grid-area: top;
  background-color: #8cffa0;
`;

export const App = styled(app)`
  grid-area: rightBottom;
  position: absolute;
  width: 75vw;
  height: 75vh;
  z-index: -10;
  background-color: red;
`;
