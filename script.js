const productListElement = document.getElementById('product-list');
const searchInput = document.getElementById('search-input');

// Function to fetch and display products
async function getProducts() {
    try {
        const response = await fetch('/products');
        const products = await response.json();

        productListElement.innerHTML = ''; // Clear existing products

        products.forEach(product => {
            const productDiv = document.createElement('div');
            productDiv.classList.add('product');
            productDiv.innerHTML = `
                <img src="" alt="${product.name}">
                <h3>${product.name}</h3>
                <p>${product.description}</p>
                <p>Price: $${product.price}</p>
                <button onclick="addToCart(${product.id})">Add to Cart</button>
            `;
            productListElement.appendChild(productDiv);
        });
    } catch (error) {
        console.error('Error fetching products:', error);
        productListElement.innerHTML = '<p>Error loading products.</p>';
    }
}

// Function to search for products
async function searchProducts() {
    const query = searchInput.value;
    try {
        const response = await fetch(`/search?q=${query}`);
        const products = await response.json();

        productListElement.innerHTML = '';

        products.forEach(product => {
            const productDiv = document.createElement('div');
            productDiv.classList.add('product');
            productDiv.innerHTML = `
                <img src="" alt="${product.name}">
                <h3>${product.name}</h3>
                <p>${product.description}</p>
                <p>Price: $${product.price}</p>
                <button onclick="addToCart(${product.id})">Add to Cart</button>
            `;
            productListElement.appendChild(productDiv);
        });
    } catch (error) {
        console.error('Error searching products:', error);
        productListElement.innerHTML = '<p>Error searching products.</p>';
    }
}

// Function to add a product to the cart (placeholder)
function addToCart(productId) {
    // In a real app, this would involve sending a request to the /cart/add endpoint
    // and updating the cart display.
    alert(`Product ${productId} added to cart!`);
}

// Initial load of products
getProducts();