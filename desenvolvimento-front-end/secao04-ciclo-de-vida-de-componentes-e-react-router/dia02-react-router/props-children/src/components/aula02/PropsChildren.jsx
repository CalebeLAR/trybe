import React from "react"
import ComponentePai from "./ComponentePai";

class PropsChildren extends React.Component {

  //para criar props children é preciso exportar funçoes. no caso de querermos "CRIAR uma NOVA TAG HTML" precisamos criar a tag em uma funcçao passar para ela a {props.children} e só aí exporta-las e usa-las. 
  render() {
    const cc = <p>asçdfkaçskdfjaçlskjdfçladf</p>
    return (
      <div className='main'>
        <ComponentePai prop={cc}>    {/*esse não é um componente real*/}
          <p>SUPIMPA</p>
          <h1>BACANA</h1>
          <span>INCRÍVEL</span>
        </ComponentePai>
      </div>
    )
  }
}
export default PropsChildren;