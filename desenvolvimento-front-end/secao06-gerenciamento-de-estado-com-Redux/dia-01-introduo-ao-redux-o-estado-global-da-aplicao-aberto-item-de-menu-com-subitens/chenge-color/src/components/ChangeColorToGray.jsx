const ChengerColorToGray = (props) => {
  const { color, changerColor } = props;
  return (
    <button
      disabled={color === "gray"}
      onClick={ ()=> changerColor("gray")}
    >
      Change to gray
    </button>
  );
};

export default ChengerColorToGray;