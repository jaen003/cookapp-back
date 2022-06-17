/* 
 * 
 * Libraries
 *
*/

using NUnit.Framework;
using preparation.src.shared.domain;

/* 
 * 
 * Class
 *
*/

namespace preparation.tests.shared {

    [TestFixture]
    public class IntValueObjectTest {

        /* 
         * 
         * Methods
         *
        */

        [Test]
        public void testIsNotAnEqualObject() {
            // Variables
            IntValueObject valueObject;
            bool           response;
            // Code
            valueObject = new IntValueObject( 3 );
            response    = valueObject.equals( new IntValueObject( 4 ) );
            Assert.IsFalse( response );
        }

        [Test]
        public void testIsAnEqualObject() {
            // Variables
            IntValueObject valueObject;
            bool           response;
            // Code
            valueObject = new IntValueObject( 3 );
            response    = valueObject.equals( new IntValueObject( 3 ) );
            Assert.IsTrue( response );
        }

        [Test]
        public void testIsAnObjectLessThan() {
            // Variables
            IntValueObject valueObject;
            bool           response;
            // Code
            valueObject = new IntValueObject( 3 );
            response    = valueObject.isLessThan( new IntValueObject( 4 ) );
            Assert.IsTrue( response );
        }

        [Test]
        public void testIsNotAnObjectLessThan() {
            // Variables
            IntValueObject valueObject;
            bool           response;
            // Code
            valueObject = new IntValueObject( 3 );
            response    = valueObject.isLessThan( new IntValueObject( 3 ) );
            Assert.IsFalse( response );
        }

        [Test]
        public void testIsNotAnObjectLessThan2() {
            // Variables
            IntValueObject valueObject;
            bool           response;
            // Code
            valueObject = new IntValueObject( 3 );
            response    = valueObject.isLessThan( new IntValueObject( 2 ) );
            Assert.IsFalse( response );
        }

        [Test]
        public void testIsAnObjectLessThanOrEqual() {
            // Variables
            IntValueObject valueObject;
            bool           response;
            // Code
            valueObject = new IntValueObject( 3 );
            response    = valueObject.isLessThanOrEqual( new IntValueObject( 3 ) );
            Assert.IsTrue( response );
        }

        [Test]
        public void testIsAnObjectLessThanOrEqual2() {
            // Variables
            IntValueObject valueObject;
            bool           response;
            // Code
            valueObject = new IntValueObject( 3 );
            response    = valueObject.isLessThanOrEqual( new IntValueObject( 4 ) );
            Assert.IsTrue( response );
        }

        [Test]
        public void testIsNotAnObjectLessThanOrEqual() {
            // Variables
            IntValueObject valueObject;
            bool           response;
            // Code
            valueObject = new IntValueObject( 3 );
            response    = valueObject.isLessThanOrEqual( new IntValueObject( 2 ) );
            Assert.IsFalse( response );
        }

        [Test]
        public void testIsAnObjectGreaterThan() {
            // Variables
            IntValueObject valueObject;
            bool           response;
            // Code
            valueObject = new IntValueObject( 4 );
            response    = valueObject.isGreaterThan( new IntValueObject( 3 ) );
            Assert.IsTrue( response );
        }

        [Test]
        public void testIsNotAnObjectGreaterThan() {
            // Variables
            IntValueObject valueObject;
            bool           response;
            // Code
            valueObject = new IntValueObject( 3 );
            response    = valueObject.isGreaterThan( new IntValueObject( 3 ) );
            Assert.IsFalse( response );
        }

        [Test]
        public void testIsNotAnObjectGreaterThan2() {
            // Variables
            IntValueObject valueObject;
            bool           response;
            // Code
            valueObject = new IntValueObject( 2 );
            response    = valueObject.isGreaterThan( new IntValueObject( 3 ) );
            Assert.IsFalse( response );
        }

        [Test]
        public void testIsAnObjectGreaterThanOrEqual() {
            // Variables
            IntValueObject valueObject;
            bool           response;
            // Code
            valueObject = new IntValueObject( 3 );
            response    = valueObject.isGreaterThanOrEqual( new IntValueObject( 3 ) );
            Assert.IsTrue( response );
        }

        [Test]
        public void testIsAnObjectGreaterThanOrEqual2() {
            // Variables
            IntValueObject valueObject;
            bool           response;
            // Code
            valueObject = new IntValueObject( 4 );
            response    = valueObject.isGreaterThanOrEqual( new IntValueObject( 3 ) );
            Assert.IsTrue( response );
        }

        [Test]
        public void testIsNotAnObjectGreaterThanOrEqual() {
            // Variables
            IntValueObject valueObject;
            bool           response;
            // Code
            valueObject = new IntValueObject( 2 );
            response    = valueObject.isGreaterThanOrEqual( new IntValueObject( 3 ) );
            Assert.IsFalse( response );
        }
    
    }

}