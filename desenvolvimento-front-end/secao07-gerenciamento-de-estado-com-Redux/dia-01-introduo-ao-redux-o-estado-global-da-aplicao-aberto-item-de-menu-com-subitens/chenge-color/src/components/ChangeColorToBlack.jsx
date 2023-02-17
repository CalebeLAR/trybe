const ChengerColorToBlack = (props) => {
  const { color, changerColor } = props;
  // para recuperar o estado da store = store.getState();
  return (
    <button
      disabled={color === "black"}
      // action seria a configuração que o dispatch recebe.
      // action: e como queremos que o estado se altere.
      // const action = "{ color: black }"

      // dipatch: é quem escreve no estado.
      // store.dispath(action)
      onClick={ ()=> changerColor("black")}
    >
      Change to black
    </button>
  );
};

export default ChengerColorToBlack;
