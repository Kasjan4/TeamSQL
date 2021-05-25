import React from 'react'
import { BrowserRouter, Switch, Route } from 'react-router-dom'

import './bootstrap/dist/css/bootstrap.min.css'
import './styles/animations.css'
import './styles/style.css'


import Home from './components/Home'


const App = () => (
  <BrowserRouter>
    <Switch>
      <Route exact path="/" component={Home} />
    </Switch>
  </BrowserRouter>
)

export default App