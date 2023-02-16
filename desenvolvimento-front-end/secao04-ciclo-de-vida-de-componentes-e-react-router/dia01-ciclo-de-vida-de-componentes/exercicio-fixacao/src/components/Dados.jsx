import '../App.css';
import React from 'react';
import unnamedgif from './unnamed.gif'
// import PropTypes from 'prop-types';

class Dados extends React.Component {
    // constructor() {
    //     super();
    // }

    render() {
        const { results } = this.props;
        return (
            <div>
                {
                    results.map((object, index) => {
                        const { name: { first, last }, email, dob: { age }, } = object;
                        return (
                            <div key={index}>
                                <div>
                                    <p>PERFIL</p>
                                    <img src={unnamedgif} alt={`${first} ${last}`} />
                                </div>
                                <div>
                                    <p>email: {email}</p>
                                    <p>idade: {age}</p>
                                    <p>nome: {`${first} ${last}`}</p>
                                </div>
                            </div>
                        )

                    })
                }
            </div>
        );
    }
}

export default Dados;

// Dados.propTypes = {
//     foto: PropTypes.string.isRequired,
//     nome: PropTypes.string.isRequired,
//     email: PropTypes.string.isRequired,
//     idade: PropTypes.string.isRequired,
//     usuário: PropTypes.string.isRequired,

// }

// Dados.defaultProps = {
//     foto: '74364e96174afa7d17ee52dd2c9c7a4651fe1254f471a78bda0190135dcd3480',
//     nome:'brad gibson',
//     email:'brad.gibson@example.com',
//     idade:'26',
//     usuário:'silverswan131',
// }
