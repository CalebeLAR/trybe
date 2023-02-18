const Block = (props) => {
  const { color } = props;
  return (
    <div 
    style={{
      backgroundColor: color,
      border: 'solid red 3px',
      width: '400px',
      height: '400px',
      margin: 'auto',
      marginTop: '30px',
      marginBottom: '30px',
    }}>

    </div>
  );
};

export default Block;