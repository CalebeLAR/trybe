/* eslint-disable max-lines-per-function */
/**
 * Para Fixar
 * Observe o código abaixo e faça as alterações necessárias para que ele passe a respeitar o Princípio da Responsabilidade Única (SRP).
*/
const readingTrackerVs1 = () => {
  type Book = {
    book: string;
    author: string;
    genre: string;
  }

  class ReadingTracker {
    private readingGoal: number;
    private booksRead: number;
    private wishlist: Book[];

    constructor(readingGoal: number) {
      this.readingGoal = readingGoal;
      this.booksRead = 0;
      this.wishlist = [];
    }

    // trackReadings(readsCount: number): void {
    //   this.booksRead += readsCount;
    //   if (this.booksRead >= this.readingGoal) {
    //     this.progressNotification(
    //       'Congratulations! You\'ve reached your reading goal!',
    //     );
    //     return;
    //   }
    //   this.progressNotification(
    //     'There are still some books to go!',
    //   );
    // }
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

    addToWishlist(book: Book): void {
      this.wishlist.push(book);
    }

    showWishlist(): void {
      console.log(this.wishlist);
    }

    // progressNotification(message: string): void {
    //   console.log(message);
    // }
  }

  const readTracker = new ReadingTracker(20);
  readTracker.addToWishlist({ book: 'The Road', author: 'Cormac McCarthy', genre: 'Dystopia' });
  readTracker.showWishlist();
  readTracker.addTrackReadings(12);
  readTracker.addTrackReadings(8);
  readTracker.assertTrackReadings();
};

readingTrackerVs1(); 