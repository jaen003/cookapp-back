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
    public class StringValueObjectTest {

        /* 
         * 
         * Methods
         *
        */

        [Test]
        public void testIsNotAnEqualObject() {
            // Variables
            StringValueObject valueObject;
            bool              response;
            // Code
            valueObject = new StringValueObject( "hello world" );
            response    = valueObject.equals( new StringValueObject( "hello world!" ) );
            Assert.IsFalse( response );
        }

        [Test]
        public void testIsAnEqualObject() {
            // Variables
            StringValueObject valueObject;
            bool              response;
            // Code
            valueObject = new StringValueObject( "hello world!" );
            response    = valueObject.equals( new StringValueObject( "hello world!" ) );
            Assert.IsTrue( response );
        }

        [Test]
        public void testIsAnEmptyObject() {
            // Variables
            StringValueObject valueObject;
            bool              response;
            // Code
            valueObject = new StringValueObject( "" );
            response    = valueObject.isEmpty();
            Assert.IsTrue( response );
        }

        [Test]
        public void testIsNotAnEmptyObject() {
            // Variables
            StringValueObject valueObject;
            bool              response;
            // Code
            valueObject = new StringValueObject( "hello world!" );
            response    = valueObject.isEmpty();
            Assert.IsFalse( response );
        }

        [Test]
        public void testIsAnObjectLongerThan() {
            // Variables
            StringValueObject valueObject;
            bool              response;
            // Code
            valueObject = new StringValueObject( "hello world!" );
            response    = valueObject.isLongerThan( new StringValueObject( "hello world" ) );
            Assert.IsTrue( response );
        }

        [Test]
        public void testIsNotAnObjectLongerThan2() {
            // Variables
            StringValueObject valueObject;
            bool              response;
            // Code
            valueObject = new StringValueObject( "hello world!" );
            response    = valueObject.isLongerThan( new StringValueObject( "hello world!" ) );
            Assert.IsFalse( response );
        }

        [Test]
        public void testIsAnObjectLongerThanOrEqual() {
            // Variables
            StringValueObject valueObject;
            bool              response;
            // Code
            valueObject = new StringValueObject( "hello world!" );
            response    = valueObject.isLongerThan( new StringValueObject( "hello world" ) );
            Assert.IsTrue( response );
        }

        [Test]
        public void testIsAnObjectLongerThanOrEqual2() {
            // Variables
            StringValueObject valueObject;
            bool              response;
            // Code
            valueObject = new StringValueObject( "hello world" );
            response    = valueObject.isLongerThanOrEqual( new StringValueObject( "hello world" ) );
            Assert.IsTrue( response );
        }

        [Test]
        public void testIsNotAnObjectLongerThanOrEqual() {
            // Variables
            StringValueObject valueObject;
            bool              response;
            // Code
            valueObject = new StringValueObject( "hello world" );
            response    = valueObject.isLongerThanOrEqual( new StringValueObject( "hello world!" ) );
            Assert.IsFalse( response );
        }

    }

}