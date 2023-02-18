import React from 'react';

class Welcome extends React.Component {
  render() {
    const { history, location } = this.props;
    return (
      <>
      <h1>Boas vindas</h1>
      <button
          type="button"
          onClick={ () => console.log(history) }
          >
          Acesse a página Home nova mente{location.pathname}
        </button>
      </>
    );
  }
}

export default Welcome;
