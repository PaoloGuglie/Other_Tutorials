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

    // Check if there are filters in place:
    if (!filters.name && !filters.price && !filters.type && !filters.brand)
    {
      return data;
    }

    for (const item of data)
    {
      // Skip the items that do not meet the criteria:

      if (filters.name !== '' && item.name !== filters.name)
      {
        continue;  // skip the item and don't add it to the filtered data.
      }

      if (filters.price !== 0 && item.price > filters.price)
      {
        continue;  // I am above max price, so I skip.
      }

      if (filters.type !== '' && item.type !== filters.type)
      {
        continue;  // same as first
      }

      if (filters.brand !== '' && item.brand !== filters.brand)
      {
        continue;  // same as first
      }

      // If all checks are passed:
      filteredData.push(item);
    }

    return filteredData;
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
      <ItemsDisplay items={filterData(data['items'])} />
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