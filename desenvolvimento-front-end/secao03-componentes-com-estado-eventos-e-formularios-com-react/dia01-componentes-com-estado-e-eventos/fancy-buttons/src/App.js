import logo from './logo.svg';
import './App.css';


function App() {
  const func1 = () => {document.getElementById('b1').innerText = `mudou b1 para: ${(Math.random() * 10).toFixed(0)}`}
  const func2 = () => {document.getElementById('b2').innerText = `mudou b2 para: ${(Math.random() * 10).toFixed(0)}`}
  const func3 = () => {document.getElementById('b3').innerText = `mudou b3 para: ${(Math.random() * 10).toFixed(0)}`}
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <button id="b1" onClick={func1}> botão 01</button>
        <button id="b2" onClick={func2}> botão 02</button>
        <button id="b3" onClick={func3}> botão 03</button>
      </header>
    </div>
  );
}

export default App;
