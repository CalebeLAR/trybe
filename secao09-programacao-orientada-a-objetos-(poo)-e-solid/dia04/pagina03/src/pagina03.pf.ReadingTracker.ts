/* eslint-disable max-classes-per-file */
/* eslint-disable @typescript-eslint/no-unused-vars */
/* eslint-disable max-lines-per-function */
/**
 * Para Fixar
 * Observe o código abaixo e faça as alterações necessárias para que ele passe a respeitar o Princípio da Responsabilidade Única (SRP).
*/
const readingTrackerVs2 = () => {
  type Book = {
    book: string;
    author: string;
    genre: string;
  }
  class WishList {
    private wishlist: Book[];
    constructor(wishlist?:Book[]) {
      this.wishlist = wishlist ?? [];
    }
  
   addToWishlist(book: Book): void {
      this.wishlist.push(book);
    }
  
    showWishlist(): void {
      console.log(this.wishlist);
    }
  }
  class ReadingTracker extends WishList {
    private readingGoal: number;
    private booksRead: number;

    constructor(readingGoal: number, wishlist?: Book[]) {
      super(wishlist);
      this.readingGoal = readingGoal;
      this.booksRead = 0;
    }

    addTrackReadings(readsCount: number): void {
      this.booksRead += readsCount;
    }

    assertTrackReadings(): void {
      if (this.booksRead >= this.readingGoal) {
        console.log(
          'Congratulations! You\'ve reached your reading goal!',
        );
        return;
      }
      console.log(
        'There are still some books to go!',
      );
    }
  }

  const wishlist01 = [
    { book: 'The Road2', author: 'Cormac McCarthy', genre: 'Dystopia' },
  ];
  const readTracker = new ReadingTracker(20);
  readTracker.showWishlist();
  readTracker.addTrackReadings(12);
  readTracker.addTrackReadings(8);
  readTracker.assertTrackReadings();
};

readingTrackerVs2();