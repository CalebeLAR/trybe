import React, { Component } from 'react'
import  PropsToDoList  from './PropsToDoList'
export default class ToDoList extends Component {
    render() {
        return (
            <div>
                <h1>Titulo pai</h1>
                <PropsToDoList>
                    <h1>ToDoList</h1>
                    <p>iniciando teste de props.children</p>
                    <p>testando como se faz para passar props children</p>
                    <p>baixando extensão que auto completa o texo</p>
                    <span>passando extensões para as props</span>
                </PropsToDoList>
            </div>
        )
    }
}


