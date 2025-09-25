interface IProduct {
  name: string;
  quantity: number;
}

interface IShoppingCartManager {
  add(name: string, quantity: number): void;
  viewCart(): void;
}

// hungry mode
class ShoppingCartManager implements IShoppingCartManager {
  private static instance = new ShoppingCartManager();
  private products: IProduct[] = [];

  private constructor() {}

  static getInstance() {
    return ShoppingCartManager.instance;
  }

  add(name: string, quantity: number) {
    this.products.push({ name, quantity });
  }

  viewCart() {
    this.products.forEach(({ name, quantity }) => {
      console.log(name, quantity);
    });
  }
}

// (function () {
//   const instance = ShoppingCartManager.getInstance();

//   instance.add("Apple", 3);
//   instance.add("Banana", 2);
//   instance.add("Orange", 5);
//   instance.viewCart();
// })();

const instance = ShoppingCartManager.getInstance();

instance.add("Apple", 3);
instance.add("Banana", 2);
instance.add("Orange", 5);
instance.viewCart();
