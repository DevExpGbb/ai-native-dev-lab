/**
 * Shopping Cart Module
 * 
 * A sample module for practicing documentation and testing workflows.
 * This code intentionally lacks comprehensive documentation and tests.
 */

export interface Product {
    id: string;
    name: string;
    price: number;
    quantity: number;
}

export interface CartItem {
    product: Product;
    quantity: number;
}

export interface Discount {
    code: string;
    type: 'percentage' | 'fixed';
    value: number;
    minPurchase?: number;
}

export class ShoppingCart {
    private items: CartItem[] = [];
    private discount: Discount | null = null;

    addItem(product: Product, quantity: number = 1): void {
        const existingItem = this.items.find(item => item.product.id === product.id);

        if (existingItem) {
            existingItem.quantity += quantity;
        } else {
            this.items.push({ product, quantity });
        }
    }

    removeItem(productId: string): boolean {
        const index = this.items.findIndex(item => item.product.id === productId);
        if (index > -1) {
            this.items.splice(index, 1);
            return true;
        }
        return false;
    }

    updateQuantity(productId: string, quantity: number): boolean {
        if (quantity < 0) {
            throw new Error('Quantity cannot be negative');
        }

        if (quantity === 0) {
            return this.removeItem(productId);
        }

        const item = this.items.find(item => item.product.id === productId);
        if (item) {
            item.quantity = quantity;
            return true;
        }
        return false;
    }

    getItems(): CartItem[] {
        return [...this.items];
    }

    getItemCount(): number {
        return this.items.reduce((total, item) => total + item.quantity, 0);
    }

    getSubtotal(): number {
        return this.items.reduce(
            (total, item) => total + item.product.price * item.quantity,
            0
        );
    }

    applyDiscount(discount: Discount): boolean {
        const subtotal = this.getSubtotal();

        if (discount.minPurchase && subtotal < discount.minPurchase) {
            return false;
        }

        this.discount = discount;
        return true;
    }

    removeDiscount(): void {
        this.discount = null;
    }

    getDiscountAmount(): number {
        if (!this.discount) return 0;

        const subtotal = this.getSubtotal();

        if (this.discount.type === 'percentage') {
            return subtotal * (this.discount.value / 100);
        } else {
            return Math.min(this.discount.value, subtotal);
        }
    }

    getTotal(): number {
        return this.getSubtotal() - this.getDiscountAmount();
    }

    clear(): void {
        this.items = [];
        this.discount = null;
    }

    isEmpty(): boolean {
        return this.items.length === 0;
    }
}

export function formatPrice(amount: number, currency: string = 'USD'): string {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: currency,
    }).format(amount);
}

export function calculateTax(amount: number, taxRate: number): number {
    if (taxRate < 0 || taxRate > 100) {
        throw new Error('Tax rate must be between 0 and 100');
    }
    return amount * (taxRate / 100);
}

export function validateProduct(product: Partial<Product>): string[] {
    const errors: string[] = [];

    if (!product.id || product.id.trim() === '') {
        errors.push('Product ID is required');
    }

    if (!product.name || product.name.trim() === '') {
        errors.push('Product name is required');
    }

    if (product.price === undefined || product.price < 0) {
        errors.push('Product price must be a non-negative number');
    }

    if (product.quantity !== undefined && product.quantity < 0) {
        errors.push('Product quantity must be a non-negative number');
    }

    return errors;
}
