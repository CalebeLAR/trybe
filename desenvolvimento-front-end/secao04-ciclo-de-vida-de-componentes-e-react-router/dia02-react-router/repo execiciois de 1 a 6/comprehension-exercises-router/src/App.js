import React, { Component } from 'react';
import Home from './components/Home';
import About from './components/About'
import Users from './components/Users'
import { BrowserRouter, Link, Redirect, Route, Switch } from 'react-router-dom';
import StrictAccess from './strict-access';

class App extends Component {
  render() {
    const user = {name:'João', password: '1234'};
    return (
      <BrowserRouter >
        <Switch>
          <Route exact path="/">
            <Home nome="prop passada no componente home do App.js">
              <Link to="/about">
                <p>About</p>
              </Link>
              <Link exact to="/">
                <p>Home</p>
              </Link>
              <Link exact to="/users">
                <p>Users</p>
              </Link>
              <Link to="/strict-access">
                <p>StrictAccess</p>
              </Link>
            </Home>
          </Route>

          <Route path="/about" component={About} />

          {/* <Route path="/users" component={Users} /> */}

          {/* 

        ----passando via props.children do Route
        <Route path="/users">
          <Users greetingsMessage="Be Welcome"/>
        </Route>

        */}


          {/* 
        ----passando via render como uma props em Users 
        <Route path="/users" render={()=>(<Users greetingsMessage={"Be welcome"} />)}/> 
        */}
          <Route path="/users/:UsersID" render={(props) => (<Users {...props} greetingsMessage={"Be welcome"} />)} />
          <Route path="/strict-access" render={()=>{
            if(user.name === 'João' && user.password === '12s34'){
              return <StrictAccess user={user}/>
            } else {
              window.alert("Access denied")
              return <Redirect to="/users/calebe"/>
            }
          }}/>
        </Switch>
      </BrowserRouter>
    );
  }
}

export default App;
