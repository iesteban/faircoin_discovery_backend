import React from 'react';
import { render } from 'react-dom';
import { Router, Route, hashHistory } from 'react-router'

import User from './modules/User'
import Feed from './modules/Feed'
import App from './modules/App'
import About from './modules/About'
import Service from './modules/Service'
import Profile from './modules/Profile'

const dest = document.getElementById('react-app');

render((
  <Router history={hashHistory}>
    <Route path="/" component={App}>
      <Route path="/user/:id" component={User}/>
      <Route path="/about" component={About}/>
      <Route path="/service/:id" component={Service}/>
      <Route path="/profile" component={Profile}/>
    </Route>
  </Router>
), dest)
