import { useState } from "react";

function AddItem(props)
{
  const [name, setName] = useState('');
  const [price, setPrice] = useState(0);
  const [type, setType] = useState('');
  const [brand, setBrand] = useState('');

  const addItemButtonPress = () =>
  {
    props.addItem({
      name: name,
      price: price,
      type: type,
      brand: brand
    });

    // Clear the state:
    setName('');
    setPrice(0);
    setType('');
    setBrand('');
  }

  return(
    <div className="container">
      <div className="row">
        <h2>Add an Item</h2>
      </div>
      <div className="row">
        <label htmlFor="name-field">Name:</label>
        <input id="name-field" type="text"
        value={name} onChange={e => setName(e.target.value)} />

        <label htmlFor="price-field">Price:</label>
        <input id="price-field" type="number"
        value={price} onChange={e => setPrice(e.target.value)} />

        <label htmlFor="type-field">Type:</label>
        <input id="type-field" type="text"
        value={type} onChange={e => setType(e.target.value)} />

        <label htmlFor="brand-field">Brand:</label>
        <input id="brand-field" type="text"
        value={brand} onChange={e => setBrand(e.target.value)} />
      </div>
      <div className="row">  
        <button type="button" onClick={addItemButtonPress}>Add Item</button>
      </div>

      
    </div>
  );
}

export default AddItem;