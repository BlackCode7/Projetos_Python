import React, { Component } from 'react'
import api from './api'

class App extends Component {
  state = {
    tweets: [],
  }

  async componentDidMount() {
    const response = await api.get('');    
    this.setState({ tweets: response.data});
}
  render() {
    const { tweets } = this.state;
    return (
      <div>
        <h1>Listar</h1>
        {console.log(tweets)};
        {tweets.map(tweet =>(
          <li key={tweet.show.id}>
            <h2>
              <strong>Título do tweet: </strong>
              {tweet.show.nome}
              {tweet.show.comentario}
              {tweet.show.data}
            </h2>
          </li>
        ))}
      </div>
    )
  }
}

export default App;
