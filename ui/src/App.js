import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import 'react-bulma-components/dist/react-bulma-components.min.css';
import { Navbar } from 'react-bulma-components';
// import Navbar from 'react-bulma-components/lib/components/navbar';

class App extends Component {
  state = {
    open: false
  }

  render() {
    const { open } = this.state
    return (
      <div className="App">
        <Navbar>
          <Navbar.Brand>
        <Navbar.Item renderAs="a" href="#">
          <img
            src="https://bulma.io/images/bulma-logo.png"
            alt="Bulma: a modern CSS framework based on Flexbox"
            width="112"
            height="28"
          />
        </Navbar.Item>
        <Navbar.Burger
          active={open}
          onClick={() =>
            this.setState(state => ({
              open: !open
            }))
          }
        />
      </Navbar.Brand>
      <Navbar.Menu active={open}>
        <Navbar.Container>
          <Navbar.Item href="#">Second</Navbar.Item>
        </Navbar.Container>
        <Navbar.Container position="end">
          <Navbar.Item href="#">At the end</Navbar.Item>
        </Navbar.Container>
      </Navbar.Menu>
        </Navbar>
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

export default App;
