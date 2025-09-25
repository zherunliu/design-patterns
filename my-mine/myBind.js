Function.prototype.myBind = function (thisArg, ...args) {
  // 返回绑定的新函数，合并绑定和新传入的参数
  return (...reArgs) => this.call(thisArg, ...args, ...reArgs);
};

function add(...args) {
  console.log(this);
  return args.reduce((prev, cur) => prev + cur, 0);
}

rico = { dislike: "JavaScript" };
const bindFunc = add.myBind(rico, 1, 2);
console.log(bindFunc(3, 4));
