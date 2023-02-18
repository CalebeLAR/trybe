import Home from './componentes/Home';
import About from './componentes/About';
import HowTo from './componentes/HowTo'
import Profile from './componentes/Profile'
import { BrowserRouter, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Route exact path="/" component={Home} />
      <Route path="/howto" component={HowTo} />
      <Route path="/about" component={About} />
      <Route path="/profile" component={Profile} />
    </BrowserRouter>
  )
};

export default App;
