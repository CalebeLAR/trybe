import React, { Component } from 'react';
import clonePerfil from './clonePerfil.png';
import { Link } from 'react-router-dom';
import '../App.css'

export default class Profile extends Component {
    render() {
        return (
            <>
                <h1>Profile</h1>
                <p>profile profile profile</p>
                <div>
                    <img src={clonePerfil} alt="clone"/>
                    <br />
                    <p>props do perfil: </p>
                    <span className='paragrafoAzul'>{this.props.name}</span>

                    <div style={{ backgroundColor: '#82F38C'}}>
                      <ul>Ships:</ul>
                      <li>proirmeira ship: {this.props.match.params.ship}</li>
                    </div>


                <Link to="/">
                    <h1>Voltar à HomePage</h1>
                </Link>
                </div>
            </>
        )
    }
}
