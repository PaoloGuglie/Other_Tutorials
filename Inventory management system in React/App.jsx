import SearchBar from "./SearchBar.jsx";
import AddItem from "./AddItem.jsx";
import ItemsDisplay from "./ItemsDisplay.jsx";

import { useState } from "react";

function App()
{
  const [filters, setFilters] = useState({});

  const [data, setData] = useState({items: []});

  const updateFilters = searchParams =>
  {
    setFilters(searchParams);
  };

  const filterData = data =>
  {
    const filteredData = [];

    for (const i of data)

    return filterData;
  }

  const addItem = item =>
  {
    // Restore the state into a variable:
    let items = data['items'];

    // Create the id field based on the length of the items array
    // (first item has arrayLenght = 0, second = 1...):
    item.id = items.length + 1;

    // Push the data into the variable:
    items.push(item);

    // Update the state:
    setData({items: items});
  };

  return (
  <div className="container">
    <div className="row mt-3">
      <ItemsDisplay items={filteredData(data['items'])} />
    </div>
    <div className="row mt-3">
      <SearchBar updateSearchParams={updateFilters} />
    </div>
    <div className="row mt-3">
      <AddItem addItem={addItem} />
    </div>
  </div>);
}

export default App;