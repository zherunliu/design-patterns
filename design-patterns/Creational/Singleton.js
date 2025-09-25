import { createInterface } from "readline";
// const { createInterface } = require("readline")

const rl = createInterface({
  input: process.stdin,
  output: process.stdout,
});

const PRIVATE_KEY = Symbol();

// lazy mode
class ShoppingCartManager {
  static #instance; // private
  #products = [];

  // 构造函数使用 PRIVATE_KEY 设置为私有
  constructor(key) {
    if (key !== PRIVATE_KEY) {
      throw new Error("Only one instance of Singleton class is allowed.");
    }
  }

  static getInstance() {
    if (!ShoppingCartManager.#instance) {
      ShoppingCartManager.#instance = new ShoppingCartManager(PRIVATE_KEY);
    }
    return ShoppingCartManager.#instance;
  }

  add(name, quantity) {
    this.#products.push({ name, quantity });
  }

  viewCart() {
    if (this.#products.length === 0) {
      return;
    }
    this.#products.forEach((product) => {
      console.log(`${product.name} ${product.quantity}`);
    });
  }
}

const cartList = [];
rl.on("line", (line) => {
  cartList.push(line.split(" "));
});

rl.on("pause", () => {
  // 暂停时才处理输出逻辑，写在函数外会直接执行
  cart = ShoppingCartManager.getInstance();
  for (let x of cartList) {
    cart.add(...x);
  }
  cart.viewCart();
  rl.close();
});
