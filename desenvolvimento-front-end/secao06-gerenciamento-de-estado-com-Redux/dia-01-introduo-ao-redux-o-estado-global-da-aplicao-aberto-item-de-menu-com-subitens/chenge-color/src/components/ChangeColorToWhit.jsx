const ChengerColorToWhite = (props) => {
  const { color, changerColor } = props;
  return (
    <button
      disabled={color === "white"}
      onClick={ ()=> changerColor("white")}
    >
      Change to white
    </button>
  );
};

export default ChengerColorToWhite;